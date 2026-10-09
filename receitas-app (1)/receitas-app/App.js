import React, { useState } from 'react';
import {
  Text,
  View,
  Button,
  StyleSheet,
  Modal,
  ScrollView,
  TouchableOpacity,
  TextInput,
  Alert,
  FlatList
} from 'react-native';

export default function App() {
  // Lista inicial de receitas
  const [listaReceitas, setListaReceitas] = useState([
    {
      id: '1',
      nome: 'Bolo de Cenoura com Cobertura de Chocolate',
      ingredientes: `3 cenouras médias picadas\n3 ovos\n1 xícara de óleo\n2 xícaras de açúcar\n2 xícaras de farinha de trigo\n1 colher (sopa) de fermento em pó`,
      modoPreparo: `1. Bata no liquidificador a cenoura, ovos e óleo.\n2. Misture o açúcar e a farinha em uma tigela.\n3. Junte as misturas, adicione o fermento e mexa delicadamente.\n4. Asse em forno pré-aquecido a 180°C por 40 minutos.`
    }
  ]);

  // Estados dos Modais
  const [modalVerVisivel, setModalVerVisivel] = useState(false);
  const [modalCadastroVisivel, setModalCadastroVisivel] = useState(false);

  // Receita selecionada para ser exibida no Modal "Ver Receita"
  const [receitaSelecionada, setReceitaSelecionada] = useState(null);

  // Estado para controlar a edição de receitas (Requisito 3)
  const [idEdicao, setIdEdicao] = useState(null);

  // Estados dos campos do formulário
  const [nome, setNome] = useState('');
  const [ingredientes, setIngredientes] = useState('');
  const [modoPreparo, setModoPreparo] = useState('');

  // Função para abrir o modal de visualização de uma receita específica
  const abrirVisualizacao = (receita) => {
    setReceitaSelecionada(receita);
    setModalVerVisivel(true);
  };

  // Preenche os campos e abre o modal para edição (Requisito 3)
  const handleIniciarEdicao = (receita) => {
    setIdEdicao(receita.id);
    setNome(receita.nome);
    setIngredientes(receita.ingredientes);
    setModoPreparo(receita.modoPreparo);

    // Fecha o modal de visualização se ele estiver aberto
    setModalVerVisivel(false);
    setModalCadastroVisivel(true);
  };

  // Função para salvar (Cadastrar ou Editar) receita (Requisito 3)
  const handleSalvar = () => {
    if (!nome.trim() || !ingredientes.trim() || !modoPreparo.trim()) {
      Alert.alert('Atenção', 'Por favor, preencha todos os campos!');
      return;
    }

    if (idEdicao !== null) {
      // Modo Edição: Atualiza os dados do item com ID correspondente via .map()
      setListaReceitas((receitasAnteriores) =>
        receitasAnteriores.map((item) =>
          item.id === idEdicao
            ? { ...item, nome, ingredientes, modoPreparo }
            : item
        )
      );
      Alert.alert('Sucesso', 'Receita atualizada com sucesso!');
    } else {
      // Modo Cadastro: Cria nova receita
      const novaReceita = {
        id: Date.now().toString(),
        nome,
        ingredientes,
        modoPreparo
      };
      setListaReceitas((receitasAnteriores) => [...receitasAnteriores, novaReceita]);
      Alert.alert('Sucesso', 'Receita cadastrada com sucesso!');
    }

    limparFormularioECFechar();
  };

  // Função para cancelar a operação
  const cancelarCadastro = () => {
    limparFormularioECFechar();
  };

  // Limpa os campos, reseta idEdicao para null e fecha o modal
  const limparFormularioECFechar = () => {
    setNome('');
    setIngredientes('');
    setModoPreparo('');
    setIdEdicao(null);
    setModalCadastroVisivel(false);
  };

  // Função para excluir receita com confirmação
  const handleExcluir = (id) => {
    Alert.alert(
      'Confirmar Exclusão',
      'Tem certeza que deseja excluir esta receita?',
      [
        {
          text: 'Cancelar',
          style: 'cancel'
        },
        {
          text: 'Excluir',
          style: 'destructive',
          onPress: () => {
            setListaReceitas((receitasAnteriores) =>
              receitasAnteriores.filter((item) => item.id !== id)
            );
            setModalVerVisivel(false);
          }
        }
      ]
    );
  };

  // Componente exibido quando a lista está vazia
  const renderEmptyList = () => (
    <View style={styles.emptyContainer}>
      <Text style={styles.emptyText}>
        📖 Nenhuma receita cadastrada. Toque no + para adicionar!
      </Text>
    </View>
  );

  return (
    <View style={styles.container}>
      <Text style={styles.title}>📱 App de Receitas</Text>
      <Text style={styles.subtitle}>Colecione suas receitas preferidas</Text>

      {/* Lista de Receitas com FlatList */}
      <FlatList
        data={listaReceitas}
        keyExtractor={(item) => item.id}
        style={styles.listContainer}
        contentContainerStyle={styles.listContent}
        showsVerticalScrollIndicator={false}
        ListEmptyComponent={renderEmptyList}
        renderItem={({ item }) => (
          <View style={styles.card}>
            <Text style={styles.cardTitle}>{item.nome}</Text>
            <View style={styles.cardActionsRow}>
              <View style={styles.cardButtonWrapper}>
                <Button title="Ver" onPress={() => abrirVisualizacao(item)} color="#007AFF" />
              </View>
              <View style={styles.cardButtonWrapper}>
                <Button title="Editar" onPress={() => handleIniciarEdicao(item)} color="#FF9500" />
              </View>
              <View style={styles.cardButtonWrapper}>
                <Button title="Excluir" color="#D9534F" onPress={() => handleExcluir(item.id)} />
              </View>
            </View>
          </View>
        )}
      />

      {/* MODAL 1: Ver Receita */}
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalVerVisivel}
        onRequestClose={() => setModalVerVisivel(false)}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContainer}>
            {receitaSelecionada && (
              <ScrollView showsVerticalScrollIndicator={false}>
                <Text style={styles.recipeTitle}>{receitaSelecionada.nome}</Text>

                <Text style={styles.sectionHeader}>🛒 Ingredientes</Text>
                <Text style={styles.recipeText}>{receitaSelecionada.ingredientes}</Text>

                <Text style={styles.sectionHeader}>👨‍🍳 Modo de Preparo</Text>
                <Text style={styles.recipeText}>{receitaSelecionada.modoPreparo}</Text>
              </ScrollView>
            )}

            <View style={styles.modalActionsRow}>
              <View style={styles.modalButtonWrapper}>
                <Button
                  title="Editar"
                  color="#FF9500"
                  onPress={() => receitaSelecionada && handleIniciarEdicao(receitaSelecionada)}
                />
              </View>
              <View style={styles.modalButtonWrapper}>
                <Button
                  title="Excluir"
                  color="#D9534F"
                  onPress={() => receitaSelecionada && handleExcluir(receitaSelecionada.id)}
                />
              </View>
              <View style={styles.modalButtonWrapper}>
                <Button title="Fechar" onPress={() => setModalVerVisivel(false)} color="#6C757D" />
              </View>
            </View>
          </View>
        </View>
      </Modal>

      {/* MODAL 2: Cadastrar/Editar Receita */}
      <Modal
        animationType="slide"
        transparent={true}
        visible={modalCadastroVisivel}
        onRequestClose={cancelarCadastro}
      >
        <View style={styles.modalOverlay}>
          <View style={styles.modalContainer}>
            {/* Título alterado dinamicamente dependendo do estado idEdicao */}
            <Text style={styles.modalHeaderTitle}>
              {idEdicao !== null ? '✏️ Editar Receita' : '📝 Cadastrar Receita'}
            </Text>

            <ScrollView showsVerticalScrollIndicator={false}>
              <Text style={styles.label}>Nome da Receita:</Text>
              <TextInput
                style={styles.input}
                placeholder="Ex: Bolo de Cenoura"
                value={nome}
                onChangeText={setNome}
              />

              <Text style={styles.label}>Ingredientes:</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                placeholder="Ex: 3 cenouras, 3 ovos, 2 xícaras de açúcar..."
                value={ingredientes}
                onChangeText={setIngredientes}
                multiline={true}
                numberOfLines={4}
                textAlignVertical="top"
              />

              <Text style={styles.label}>Modo de Preparo:</Text>
              <TextInput
                style={[styles.input, styles.textArea]}
                placeholder="Ex: 1. Bata a cenoura e os ovos no liquidificador..."
                value={modoPreparo}
                onChangeText={setModoPreparo}
                multiline={true}
                numberOfLines={4}
                textAlignVertical="top"
              />
            </ScrollView>

            <View style={styles.formButtonRow}>
              <View style={styles.buttonWrapper}>
                <Button title="Cancelar" onPress={cancelarCadastro} color="#D9534F" />
              </View>
              <View style={styles.buttonWrapper}>
                <Button title="Salvar" onPress={handleSalvar} color="#28A745" />
              </View>
            </View>
          </View>
        </View>
      </Modal>

      {/* Botão Flutuante (FAB) */}
      <TouchableOpacity
        style={styles.fab}
        onPress={() => {
          limparFormularioECFechar();
          setModalCadastroVisivel(true);
        }}
        activeOpacity={0.8}
      >
        <Text style={styles.fabText}>+</Text>
      </TouchableOpacity>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    paddingTop: 50,
    backgroundColor: '#BAB5B5',
    alignItems: 'center',
  },
  title: {
    fontSize: 32,
    fontWeight: 'bold',
    marginBottom: 5,
    textAlign: 'center',
  },
  subtitle: {
    fontSize: 20,
    marginBottom: 15,
    textAlign: 'center',
  },

  // FlatList & Cartões
  listContainer: {
    width: '100%',
  },
  listContent: {
    paddingHorizontal: 20,
    paddingBottom: 90,
  },
  card: {
    backgroundColor: '#FFF',
    padding: 18,
    borderRadius: 12,
    marginBottom: 15,
    elevation: 3,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.2,
    shadowRadius: 3,
  },
  cardTitle: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 12,
  },
  cardActionsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
  },
  cardButtonWrapper: {
    flex: 0.31,
  },

  // Estado da Lista Vazia
  emptyContainer: {
    padding: 25,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#FFF',
    borderRadius: 12,
    marginTop: 20,
  },
  emptyText: {
    fontSize: 16,
    color: '#666',
    textAlign: 'center',
    lineHeight: 22,
  },

  // Estilos Gerais dos Modais
  modalOverlay: {
    flex: 1,
    backgroundColor: 'rgba(0, 0, 0, 0.5)',
    justifyContent: 'center',
    alignItems: 'center',
    padding: 20,
  },
  modalContainer: {
    width: '100%',
    maxHeight: '85%',
    backgroundColor: '#FFF',
    borderRadius: 15,
    padding: 20,
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.25,
    shadowRadius: 4,
  },

  // Modal Ver Receita
  recipeTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 10,
    textAlign: 'center',
  },
  sectionHeader: {
    fontSize: 18,
    fontWeight: 'bold',
    color: '#007AFF',
    marginTop: 15,
    marginBottom: 8,
  },
  recipeText: {
    fontSize: 15,
    color: '#444',
    lineHeight: 22,
  },
  modalActionsRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 15,
  },
  modalButtonWrapper: {
    flex: 0.31,
  },

  // Modal Cadastro/Edição
  modalHeaderTitle: {
    fontSize: 22,
    fontWeight: 'bold',
    color: '#333',
    marginBottom: 15,
    textAlign: 'center',
  },
  label: {
    fontSize: 15,
    fontWeight: 'bold',
    color: '#444',
    marginTop: 10,
    marginBottom: 5,
  },
  input: {
    backgroundColor: '#F5F5F5',
    borderWidth: 1,
    borderColor: '#DDD',
    borderRadius: 8,
    padding: 10,
    fontSize: 15,
  },
  textArea: {
    minHeight: 80,
  },
  formButtonRow: {
    flexDirection: 'row',
    justifyContent: 'space-between',
    marginTop: 20,
  },
  buttonWrapper: {
    flex: 0.48,
  },

  // Botão Flutuante (FAB)
  fab: {
    position: 'absolute',
    bottom: 24,
    right: 24,
    width: 60,
    height: 60,
    borderRadius: 30,
    alignItems: 'center',
    justifyContent: 'center',
    backgroundColor: '#007AFF',
    elevation: 5,
    shadowColor: '#000',
    shadowOffset: { width: 0, height: 2 },
    shadowOpacity: 0.3,
    shadowRadius: 3,
  },
  fabText: {
    fontSize: 28,
    color: '#fff',
    fontWeight: 'bold',
  },
});

